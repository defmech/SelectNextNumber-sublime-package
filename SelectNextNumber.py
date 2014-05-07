import sublime, sublime_plugin

class SelectNextNumberCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].end()
		region = self.view.find('(?:\d*\.)?\d+', pos)
		self.view.sel().clear()
		self.view.sel().add(region)
