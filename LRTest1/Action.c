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
	
	
	//���뼯�ϵ㣬Ҳ���Ƕ���û����е������ʱ�򣬻���еȴ���Ȼ��һ��ִ������Ĵ��룬���ǲ���
	// Ҫ��������֮ǰ
	
	lr_rendezvous("login_Rendezvous");

	
	lr_start_transaction("auto_transaction");
	
	//�˴���ʼ����
	lr_start_transaction("login_transaction");
	
	//���㣬�൱�ڡ����ԡ������Ǽ�������ѹ����ʱ������ܷ���ȷ����ָ���Ĳ��Զ���
	web_reg_find("Text=Welcome",
		LAST);
	
	
	web_submit_form("login.pl",
	                "Snapshot=t4.inf",
	                ITEMDATA,
	                //�����������ǰ�ĳ�������滻Ϊ�������ͣ�Ŀ���������û��ܹ���ʵ��ģ����ʵ�û�����ϵͳ�Ĳ���
	                "Name=username","Value={username}",ENDITEM,
	                "Name=password","Value=bean",ENDITEM,
	                "Name=login.x","Value=46",ENDITEM,
	                "Name=login.y","Value=12",ENDITEM,
	                LAST);
	lr_end_transaction("login_transaction",LR_AUTO);
	
	lr_end_transaction("auto_transaction", LR_AUTO);
	
	return 0;
}
