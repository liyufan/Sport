import wx
import sport
import pymysql


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
		a_name = self.m_name1.GetValue()
		a_no = self.m_no1.GetValue()
		e = self.m_event1.GetValue()  # 项目名为汉字
		score = int(self.m_score1.GetValue())

		sql = "SELECT Eno FROM EVENT WHERE Ename LIKE %s"  # 防止SQL注入
		self.cursor.execute(sql, e)
		result = self.cursor.fetchall()
		event_no = result[0]  # 返回项目名称对应的编号

		sql = "SELECT * FROM SCORE WHERE Ano = %s AND Eno = %s"
		exist = self.cursor.execute(sql, (a_no, event_no))
		if exist:
			try:
				sql = "INSERT INTO SCORE VALUE (%s, %s, %s)"
				self.cursor.execute(sql, (a_no, event_no, score))
				self.db.commit()
				self.m_statusBar.SetStatusText("已成功更新1条数据", 1)
			except Exception:
				self.db.rollback()
				self.m_statusBar.SetStatusText("操作失败！", 1)
		else:
			try:
				sql = "UPDATE SCORE SET Score = %s WHERE Ano = %s AND Eno = %s"
				self.cursor.execute(sql, (score, a_no, event_no))
				self.db.commit()
				self.m_statusBar.SetStatusText("已成功插入1条数据", 1)
			except Exception:
				self.db.rollback()
				self.m_statusBar.SetStatusText("操作失败！", 1)

	def delete(self, event):
		pass

	def query(self, event):
		i = self.m_choice.GetSelection()  # 0代表学生姓名，1代表项目名称
		condition = self.m_input.GetValue()
		if i == 0:
			sql = "SELECT Ano FROM ATHLETE WHERE Aname LIKE %S"
			self.cursor.execute(sql, condition)
			result = self.cursor.fetchall()
			a_no = result[0]

			sql = "SELECT * FROM SCORE WHERE Ano = %s"
			self.cursor.execute(sql, a_no)
			result = self.cursor.fetchall()  # 查询结果不多于4条

	def exit(self, event):
		self.exit()

	def info(self, event):
		self.m_statusBar.SetStatusText("版本：0.2", 1)


if __name__ == '__main__':
	# 下面是使用wxPython的固定用法
	app = wx.App()

	main_win = MainSport(None)
	main_win.Show()

	app.MainLoop()
