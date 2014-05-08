import sublime, sublime_plugin

class SelectNextNumberCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].end()
		region = self.view.find('(?:\d*\.)?\d+', pos)

		if region.a == -1:
			region.a = pos
			region.b = pos

		self.view.sel().clear()
		self.view.sel().add(region)
