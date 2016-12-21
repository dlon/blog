import web
import markdown

urls = (
	'/(.*)', 'page'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class page:
	def GET(self, url):
		if url == '' or url == '/':
			url = 'index'
		# handle markdown pages
		try:
			f = open("pages/{}.md".format(url))
			html = markdown.markdown(f.read())
			f.close()
			return render.markdown('title', html)
		except IOError:
			raise web.notfound()

if __name__ == "__main__":
	app.run()