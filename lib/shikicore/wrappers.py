from . import Api

api = None

def authorize(login, password, token=None):
	global api
	api = Api(login, password, token=token)
	
	return api.token

def list():
	return api.animes().get()
	
def ongoing(limit=20, page=1):
	return api.animes(status='ongoing', limit=limit, page=page).get()

def animes_search(s, limit=20, page=1):
	return api.animes(search=s, limit=limit, page=page).get()

def by_year(year, limit=20, page=1):
	return api.animes(status='released', season=year, limit=limit, page=page).get()

def genres():
	return api.genres().get()

def by_genre(genre, limit=20, page=1):
	return api.animes(genre=genre, limit=limit, page=page).get()

def animes_screenshots(id):
	try:
		return api.animes('%s/screenshots' % str(id)).get()
	except ValueError:
		return []


def animes_(id):
	try:
		return api.animes('%s' % str(id)).get()
	except ValueError:
		return {}

def animes_roles(id):
	try:
		return api.animes('%s/roles' % str(id)).get()
	except ValueError:
		return []

def animes_similar(id):
	try:
		return api.animes('%s/similar' % str(id)).get()
	except ValueError:
		return []

def animes_related(id):
	try:
		return api.animes('%s/related' % str(id)).get()
	except ValueError:
		return []
