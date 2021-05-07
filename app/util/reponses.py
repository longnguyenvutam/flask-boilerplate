BAD_REQUEST={
	'status':False,
	'code':400,
	'message':'Bad request'
}

CREATED={
	'status':False,
	'code':201,
	'message':'Created'
}

UNAUTHORIZED_ACCESS={
	'status':False,
	'code': 401,
	'message':'Unauthorized access'
}

INTERNAL_SERVER_ERROR={
	'status':False,
	'code':501,
	'message':'Internal server error'
}

INVALID_USER={
	'status':False,
	'code':401,
	'message': "Username or Password is wrong"
}

VALID_USER={
	'status':False,
	'code':200,
	'message':"User login successfully"
}

LOGINED={
	'status':False,
	'code':200,
	'message':'Already logined'
}

LOGOUT={
	'status':False,
	'code':200,
	'message':'Logout successfully'
}

def cre_msg(msg,data):
	return{
		'status':True,
		'message':msg,
		'data':data
	}