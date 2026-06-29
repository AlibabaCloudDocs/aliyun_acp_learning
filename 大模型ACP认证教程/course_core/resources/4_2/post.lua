wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"
wrk.body = [[
    {
       "model": "./model/qwen2_5-1_5b-instruct",
       "messages": [
           {"role": "system", "content": "你是一个帮助助手。"},
           {"role": "user", "content": "请告诉我2008年北京奥运会，中国队总共获得了多少枚金牌？"}
       ]
   }
]]