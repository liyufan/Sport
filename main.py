import pymysql
import wx
from pymysql.err import *

import sport


# SCORE表记录成绩
# EVENT表记录项目名称Ename与编号Eno关系，静态表，即已在运动会前定好，不会改变，且项目名称唯一
# ATHLETE表记录运动员姓名Aname与编号Ano，静态表，即已在运动会前定好，不会改变，且姓名唯一

class MainSport(sport.MyFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.db = pymysql.connect(host='localhost', user='root', passwd='*', db='s', charset='utf8')
		self.cursor = self.db.cursor()
		self.m_statusBar.SetStatusText("就绪", 0)

	def insert_update(self, event):
		a_no = self.m_no.GetValue()  # 运动员编号
		e = self.m_event.GetValue()  # 项目编号
		score = int(self.m_score.GetValue())  # 成绩
		self.m_output.Clear()

		'''
		sql = "SELECT Eno FROM EVENT WHERE Ename LIKE %s"  # 防止SQL注入
		self.cursor.execute(sql, e)
		result = self.cursor.fetchall()
		event_no = result[0]  # 返回项目名称对应的编号
		'''

		sql = "SELECT * FROM SCORE WHERE Ano = %s AND Eno = %s" % (a_no, e)  # 防止SQL注入
		# self.cursor.execute(sql, (a_no, event_no))
		self.cursor.execute(sql)
		result = self.cursor.fetchall()
		if result is None:  # 返回空值，表示不存在旧数据，为插入数据
			try:
				sql = "INSERT INTO SCORE VALUE (%s, %s, %s)" % (a_no, e, score)
				self.cursor.execute(sql)
				self.db.commit()
				self.m_statusBar.SetStatusText("已成功插入1条数据", 1)
			except DatabaseError:
				self.db.rollback()
				self.m_statusBar.SetStatusText("操作失败！", 1)
		else:  # 返回非空值，表示存在旧数据，为更新数据
			try:
				sql = "UPDATE SCORE SET Score = %s WHERE Ano = %s AND Eno = %s" % (score, a_no, e)
				self.cursor.execute(sql)
				self.db.commit()
				self.m_statusBar.SetStatusText("已成功更新1条数据", 1)
			except DatabaseError:
				self.db.rollback()
				self.m_statusBar.SetStatusText("操作失败！", 1)

	def delete(self, event):
		i = self.m_choice.GetSelection()  # 0运动员姓名 1运动员编号 2项目名 3项目编号
		condition = self.m_input.GetValue()  # 删除条件具体值
		self.m_output.Clear()
		sql = ""
		if i == 0:
			sql = "DELETE FROM SCORE WHERE Ano IN (SELECT Ano FROM ATHLETE WHERE Aname LIKE %s)" % condition
		elif i == 1:
			sql = "DELETE FROM SCORE WHERE Ano = %s" % condition
		elif i == 2:
			sql = "DELETE FROM SCORE WHERE Eno IN (SELECT Eno FROM EVENT WHERE Ename LIKE %s)" % condition
		elif i == 3:
			sql = "DELETE FROM SCORE WHERE Eno = %s" % condition
		try:
			rol = self.cursor.execute(sql)
			self.db.commit()
			self.m_statusBar.SetStatusText("已成功删除" + rol + "条数据", 1)
		except DatabaseError:
			self.db.rollback()
			self.m_statusBar.SetStatusText("删除失败！", 1)

	def query(self, event):
		i = self.m_choice.GetSelection()  # 0运动员姓名 1运动员编号 2项目名 3项目编号
		condition = self.m_input.GetValue()  # 查询条件具体值
		self.m_output.Clear()
		sql = ""
		if i == 0:
			sql = "SELECT ATHLETE.Ano, EVENT.Ename, EVENT.Eno, SCORE.Score FROM ATHLETE, EVENT, SCORE WHERE SCORE.Ano " \
			      "= ATHLETE.Ano AND SCORE.Eno = EVENT.Eno AND Aname LIKE %s " % condition
			self.m_output.AppendText("运动员编号\t项目名\t项目编号\t成绩\n")  # 按姓名查询时，输出不显示姓名

		elif i == 1:
			sql = "SELECT ATHLETE.Aname, EVENT.Ename, EVENT.Eno, SCORE.Score FROM ATHLETE, EVENT, SCORE WHERE " \
			      "SCORE.Ano = ATHLETE.Ano AND SCORE.Eno = EVENT.Eno AND Ano = %s " % condition
			self.m_output.AppendText("运动员姓名\t项目名 \t项目编号\t成绩\n")
		elif i == 2:
			sql = "SELECT ATHLETE.Ano, ATHLETE.Aname, EVENT.Eno, SCORE.Score FROM ATHLETE, EVENT, SCORE WHERE " \
			      "SCORE.Ano = ATHLETE.Ano AND SCORE.Eno = EVENT.Eno AND Ename LIKE %s " % condition
			self.m_output.AppendText("运动员编号\t运动员姓名\t项目编号\t成绩\n")
		elif i == 3:
			sql = "SELECT ATHLETE.Ano, ATHLETE.Aname, EVENT.Ename, SCORE.Score FROM ATHLETE, EVENT, SCORE WHERE " \
			      "SCORE.Ano = ATHLETE.Ano AND SCORE.Eno = EVENT.Eno AND Eno = %s " % condition
			self.m_output.AppendText("运动员编号\t运动员姓名\t项目名\t成绩\n")
		self.cursor.execute(sql)
		result = self.cursor.fetchall()
		for var in result:
			for item in var:
				self.m_output.AppendText(str(item) + '\t\t')
			self.m_output.AppendText('\n')

	def exit(self, event):
		self.cursor.close()
		self.db.close()
		self.exit()

	def info(self, event):
		self.m_statusBar.SetStatusText("版本：0.2", 1)


if __name__ == '__main__':
	# 下面是使用wxPython的固定用法
	app = wx.App()

	main_win = MainSport(None)
	main_win.Show()

	app.MainLoop()
