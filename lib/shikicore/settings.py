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
		r = authorize(uname, passw, token)
	else:
		r = authorize(uname, passw)
	core.log_error(str(r))

	if not r:
		core.addon.openSettings()
		return False
	else:
		core.token = r
		core.username_ok = uname
		core.password_ok = passw

	return True
