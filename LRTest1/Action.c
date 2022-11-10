Action()
{
	web_url("WebTours",
	        "URL=http://127.0.0.1:1080/WebTours/",
	        "Resource=0",
	        "RecContenetType=text/html",
	        "Referer=",
	        "Snapshot = t1.inf",
	        "Mode=HTML",
	        EXTRARES,
	        "Url=https://ieonline/microsoft.com/iedomainsuggestions/iell/suggestions.zh-CN",
	        "Referer=",ENDITEM,
	        "Url=https://ieonline/microsoft.com/ieflipahead/ie10/rules.xml?mkt=zh-CN",
	        "Referer=",ENDITEM,
	        LAST);
	
	lr_think_time(34);
	
	//此处开始事务
	lr_start_transaction("login_Trans");
	web_submit_form("login.pl",
	                "Snapshot = t2.inf",
	                ITEMDATA,
	                "Name=username","Value=jojo",ENDITEM,
	                "Name=password","Value=bean",ENDITEM,
	                "Name=login.x","Value=46",ENDITEM,
	                "Name=login.y","Value=12",ENDITEM,
	                LAST);
	lr_end_transaction("login_trans",LR_AUTO);
	
	return 0;
}
