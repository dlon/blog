import web
import markdown

urls = (
	'/', 'index',
	'/writings/(.+)', 'writing',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class index:
	def GET(self):
		f = open("pages/index.md")
		md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
		html = md.convert(f.read())
		f.close()
		return render.index(md.Meta, html)

class writing:
	def GET(self, url):
		if url[-1] == '/': url = url[:-1]
		try:
			f = open("pages/{}.md".format(url))
			md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
			html = md.convert(f.read())
			f.close()
			return render.writing(md.Meta, html)
		except IOError:
			raise web.notfound()

if __name__ == "__main__":
	app.run()