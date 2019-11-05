import wx

import sport


class MainWin(sport.MyFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.m_statusBar.SetStatusWidths([-1, -4])
		self.m_statusBar.SetStatusText("就绪", 0)
		self.m_statusBar.SetStatusText("已成功插入1条数据", 1)


if __name__ == '__main__':
	# 下面是使用wxPython的固定用法
	app = wx.App()

	main_win = MainWin(None)
	main_win.Show()

	app.MainLoop()
