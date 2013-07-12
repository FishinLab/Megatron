<h1>Megatron</h1>

    Megatron is a SAP automation testing tool in BPC project. You can merge XML report files, generate HTML report and send 
    e-mail showing the weekly report

    1. Megatron was formed by what?
        Megatron -- gui 
                 \-- api
                  \-- html report -- html_reportpy 
                  |               \-- history_data 
                  |                \-- deployer
                   \-- xml report -- xml_merger
                                  \-- xml_parser 
    2. How to use Megatron?                                 
        
        XML reports operation:
            setting.conf keeps parameter for merging XML report files     
            MERGER_PATH is for XML merger file path
            MERGEE_PATH is for XML mergee file path
            REPORT_PATH when we use merger file instead for the failure elements, keeps the result XML report path
            when you configure this correctly, click button which named MERGE

        HTML report operation:
            setting.conf also keeps parameter for generating HTML weekly report
            DEPLOY_SERVERS is for which server should be tested by automation tool
            DEPLOY_PATH is for the path when you generated a HTML report,  
            when you configure this correctly, click button which named DEPLOY, Megatron will do all the job for you 

contact me: fishinlab@sina.com
