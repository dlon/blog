import web
        
urls = (
	'/(.*)', 'page'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class page:
	def GET(self, name):
		return render.hello('world')

if __name__ == "__main__":
	app.run()