from . import Api

api = None

def authorize(login, password, token=None):
	global api
	api = Api(login, password, token=token)
	
	return api

def list():
	try:
		return api.animes().get()
	except ValueError:
		return []
	
def ongoing(limit=20, page=1):
	try:
		return api.animes(status='ongoing', limit=limit, page=page).get()
	except ValueError:
		return []

def whoami():
	try:
		return api.users('whoami').get()
	except ValueError:
		return None

def favourites(limit=20, page=1, _whoami=None):
	try:
		if not _whoami:
			_whoami = whoami()

		fv = api.users('%s/favourites' % _whoami['id'], limit=limit, page=page).get()
		return fv['animes']

	except ValueError:
		return []


def animes_search(s, limit=20, page=1):
	try:
		return api.animes(search=s, limit=limit, page=page).get()
	except ValueError:
		return []

def by_year(year, limit=20, page=1):
	try:
		return api.animes(status='released', season=year, limit=limit, page=page).get()
	except ValueError:
		return []

def genres():
	return api.genres().get()

def by_genre(genre, limit=20, page=1):
	try:
		return api.animes(genre=genre, limit=limit, page=page).get()
	except ValueError:
		return []

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

def user_rates(user_id=None, target_id=None, status=None):
	try:
		kwargs = {}
		if user_id:
			kwargs['user_id'] = user_id
		if target_id:
			kwargs['target_id'] = target_id
			kwargs['target_type'] = 'Anime'
		if status:
			kwargs['status'] = status

		return api.user_rates(**kwargs).get()
	except ValueError:
		return []

def prepare_user_rate(score, status, target_id, user_id):
	if not user_id:
		user_id = whoami()['id']
	
	user_rate = {'user_id': user_id}
	
	if target_id:
		user_rate['target_id'] = target_id
		user_rate['target_type'] = 'Anime'
	
	if status:
		user_rate['status'] = status
	
	if score:
		user_rate['score'] = status
	return user_rate

def create_user_rate(user_id=None, target_id=None, status=None, score=None):

	user_rate = prepare_user_rate(score, status, target_id, user_id)

	return api.user_rates(user_rate=user_rate).post()

def update_user_rate(id, user_id=None, target_id=None, status=None, score=None):
	user_rate = prepare_user_rate(score, status, target_id, user_id)

	return api.user_rates(str(id), user_rate=user_rate).patch()

def delete_user_rate(id):
	try:
		api.user_rates(str(id)).delete()
	except ValueError:
		pass
