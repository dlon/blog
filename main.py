import web
import markdown
import os

urls = (
	'/', 'index',
	'/writings/(.+)', 'writing',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class index:
	def GET(self):
		# get metadata for posts
		# [ {title, url, published, description} ] (etc.)
		meta = []
		writings = os.listdir('pages/')
		for post in writings:
			if post[-3:] != '.md':
				continue
			md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
			f = open("pages/{}".format(post))
			md.convert(f.read())
			f.close()
			md.Meta['url'] = '/writings/{}'.format(post[:-3])
			meta += [md.Meta]
		# TODO: sort by date
		return render.index(meta)

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