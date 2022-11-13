Action()
{
	web_url("WebTours",
	        "URL=http://127.0.0.1:1080/WebTours/",
	        "Resource=0",
	        "RecContentType=text/html",
	        "Referer=",
	        "Snapshot=t3.inf",
	        "Mode=HTML",
	        EXTRARES,
	        "Url=https://ieonline/microsoft.com/iedomainsuggestions/iell/suggestions.zh-CN",
	        "Referer=",ENDITEM,
	        "Url=https://ieonline/microsoft.com/ieflipahead/ie10/rules.xml?mkt=zh-CN",
	        "Referer=",ENDITEM,
	        LAST);
	
	lr_think_time(34);
	
	
	//插入集合点，也就是多个用户运行到这里的时候，会进行等待，然后一起执行下面的代码，就是并发
	// 要放在事务之前
	
	lr_rendezvous("login_Rendezvous");

	
	lr_start_transaction("auto_transaction");
	
	//此处开始事务
	lr_start_transaction("login_transaction");
	
	//检查点，相当于“断言”，就是检查服务器压力大时，检查能否真确返回指定的测试对象
	web_reg_find("Text=Welcome",
		LAST);
	
	
	web_submit_form("login.pl",
	                "Snapshot=t4.inf",
	                ITEMDATA,
	                //参数化，就是把某个参数替换为其他类型，目的是虚拟用户能够真实的模拟现实用户进行系统的操作
	                "Name=username","Value={username}",ENDITEM,
	                "Name=password","Value=bean",ENDITEM,
	                "Name=login.x","Value=46",ENDITEM,
	                "Name=login.y","Value=12",ENDITEM,
	                LAST);
	lr_end_transaction("login_transaction",LR_AUTO);
	
	lr_end_transaction("auto_transaction", LR_AUTO);
	
	return 0;
}
