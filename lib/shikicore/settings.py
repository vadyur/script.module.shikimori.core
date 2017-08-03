def authorize_me():

	from wrappers import authorize
	from simpleplugin import Plugin

	core = Plugin('script.module.shikimori.core')

	uname = core.username
	passw = core.password
	token = core.token

	uname_ok = core.username_ok
	passw_ok = core.password_ok

	if uname == uname_ok and passw == passw_ok and token:
		api = authorize(uname, passw, token)
	else:
		api = authorize(uname, passw)

	if not api.token:
		core.addon.openSettings()
		return None
	else:
		core.token = api.token
		core.username_ok = uname
		core.password_ok = passw

	return api
