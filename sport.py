# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"运动会数据库管理系统", pos=wx.DefaultPosition,
		                  size=wx.Size(826, 442), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer = wx.BoxSizer(wx.VERTICAL)

		sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"请选择功能"), wx.VERTICAL)

		bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_radioBtn1 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize,
		                                  0)
		bSizer9.Add(self.m_radioBtn1, 0, wx.ALL, 5)

		self.m_radioBtn2 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, u"插入", wx.DefaultPosition, wx.DefaultSize,
		                                  0)
		bSizer9.Add(self.m_radioBtn2, 0, wx.ALL, 5)

		sbSizer1.Add(bSizer9, 0, wx.ALIGN_CENTER, 5)

		bSizer.Add(sbSizer1, 0, wx.ALIGN_CENTER, 5)

		sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"操作"), wx.VERTICAL)

		bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText8 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
		                                   wx.DefaultSize, 0)
		self.m_staticText8.Wrap(-1)

		bSizer5.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.ALIGN_LEFT | wx.ALL, 5)

		self.m_button1 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"插入/更新", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer5.Add(self.m_button1, 0, wx.ALL, 5)

		self.m_staticText11 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"查询/删除条件：", wx.DefaultPosition,
		                                    wx.DefaultSize, 0)
		self.m_staticText11.Wrap(-1)

		bSizer5.Add(self.m_staticText11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		m_choiceChoices = [u"学生姓名", u"项目名称"]
		self.m_choice = wx.Choice(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
		                          m_choiceChoices, wx.CB_SORT)
		self.m_choice.SetSelection(0)
		bSizer5.Add(self.m_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_input = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                           wx.DefaultSize, 0)
		bSizer5.Add(self.m_input, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticText9 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
		                                   wx.DefaultSize, 0)
		self.m_staticText9.Wrap(-1)

		bSizer5.Add(self.m_staticText9, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_button2 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer5.Add(self.m_button2, 0, wx.ALL, 5)

		self.m_button3 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer5.Add(self.m_button3, 0, wx.ALL, 5)

		sbSizer2.Add(bSizer5, 1, wx.ALIGN_CENTER, 5)

		bSizer.Add(sbSizer2, 0, wx.ALIGN_CENTER, 5)

		sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"输入与结果"), wx.HORIZONTAL)

		fgSizer1 = wx.FlexGridSizer(0, 4, 0, 0)
		fgSizer1.SetFlexibleDirection(wx.BOTH)
		fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText12 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"姓名", wx.DefaultPosition,
		                                    wx.DefaultSize, 0)
		self.m_staticText12.Wrap(-1)

		fgSizer1.Add(self.m_staticText12, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticText13 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"编号", wx.DefaultPosition,
		                                    wx.DefaultSize, 0)
		self.m_staticText13.Wrap(-1)

		fgSizer1.Add(self.m_staticText13, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticText15 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"项目", wx.DefaultPosition,
		                                    wx.DefaultSize, 0)
		self.m_staticText15.Wrap(-1)

		fgSizer1.Add(self.m_staticText15, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticText16 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"成绩", wx.DefaultPosition,
		                                    wx.DefaultSize, 0)
		self.m_staticText16.Wrap(-1)

		fgSizer1.Add(self.m_staticText16, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_name1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                           wx.DefaultSize, 0)
		fgSizer1.Add(self.m_name1, 0, wx.ALL, 5)

		self.m_no1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
		                         0)
		fgSizer1.Add(self.m_no1, 0, wx.ALL, 5)

		self.m_event1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_event1, 0, wx.ALL, 5)

		self.m_score1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_score1, 0, wx.ALL, 5)

		self.m_name2 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                           wx.DefaultSize, 0)
		fgSizer1.Add(self.m_name2, 0, wx.ALL, 5)

		self.m_no2 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
		                         0)
		fgSizer1.Add(self.m_no2, 0, wx.ALL, 5)

		self.m_event2 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_event2, 0, wx.ALL, 5)

		self.m_score2 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_score2, 0, wx.ALL, 5)

		self.m_name3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                           wx.DefaultSize, 0)
		fgSizer1.Add(self.m_name3, 0, wx.ALL, 5)

		self.m_no3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
		                         0)
		fgSizer1.Add(self.m_no3, 0, wx.ALL, 5)

		self.m_event3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_event3, 0, wx.ALL, 5)

		self.m_score3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_score3, 0, wx.ALL, 5)

		self.m_name4 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                           wx.DefaultSize, 0)
		fgSizer1.Add(self.m_name4, 0, wx.ALL, 5)

		self.m_no4 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
		                         0)
		fgSizer1.Add(self.m_no4, 0, wx.ALL, 5)

		self.m_event4 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_event4, 0, wx.ALL, 5)

		self.m_score4 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
		                            wx.DefaultSize, 0)
		fgSizer1.Add(self.m_score4, 0, wx.ALL, 5)

		sbSizer3.Add(fgSizer1, 1, 0, 5)

		bSizer.Add(sbSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.SetSizer(bSizer)
		self.Layout()
		self.m_statusBar = self.CreateStatusBar(2, wx.STB_SIZEGRIP, wx.ID_ANY)
		self.m_menubar = wx.MenuBar(0)
		self.m_menu = wx.Menu()
		self.m_menuItem_quit = wx.MenuItem(self.m_menu, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menu.Append(self.m_menuItem_quit)

		self.m_menubar.Append(self.m_menu, u"菜单")

		self.m_menu_info = wx.Menu()
		self.m_menuItem_ver = wx.MenuItem(self.m_menu_info, wx.ID_ANY, u"版本", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menu_info.Append(self.m_menuItem_ver)

		self.m_menubar.Append(self.m_menu_info, u"关于")

		self.SetMenuBar(self.m_menubar)

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button1.Bind(wx.EVT_BUTTON, self.insert_update)
		self.m_button2.Bind(wx.EVT_BUTTON, self.delete)
		self.m_button3.Bind(wx.EVT_BUTTON, self.query)
		self.Bind(wx.EVT_MENU, self.exit, id=self.m_menuItem_quit.GetId())
		self.Bind(wx.EVT_MENU, self.info, id=self.m_menuItem_ver.GetId())

	def __del__(self):
		pass

	# Virtual event handlers, override them in your derived class
	def insert_update(self, event):
		event.Skip()

	def delete(self, event):
		event.Skip()

	def query(self, event):
		event.Skip()

	def exit(self, event):
		event.Skip()

	def info(self, event):
		event.Skip()
