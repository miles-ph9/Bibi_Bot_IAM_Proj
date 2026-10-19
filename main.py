
#imports
import uvicorn
from fastapi import FastAPI

# Testing area
x = "Bibi 1.0v is booting up..."

#Banner section

Banner_text1 = r"""
=========================================================
 🐇 [BiBi.SYS v1.0] - IDENTITY ACCESS CONTROL INTERFACE 🐇
=========================================================
"""
BI_BANNER = r"""

۶ .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+ 
Beep boop beep!
Welcome to Bibi's Central Hub

               ,--------------------------,
              |  ۶ৎ---------------------۶ৎ|
              | |                       | |
              | |     ●        ●        | |
              | |                       | |                
              | |         ∪             | |                  
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

=========================================================
 STATUS: Active | OPERATOR: Mylah | THREAT LEVEL: Zero
 SYSTEM LOG: Cookies accepted. Please provide an access key.
=========================================================                                                                                                                                        
 "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+

"""

DOCUMENTATION_ = f"""
<p> {Banner_text1} </pre>

```
{BI_BANNER}
 ```
<h3> Welcome to the IAM Security Control Room </h3>
<p> This mini engine, Bibi, is used to monitor active API pathways and secure your API keys from being cloned and stolen</p>

"""

app = FastAPI(
    #heading of the webpage
    title = "Bibi IAM Authentication Platform",
    version = "1.0",
   #Prints summaries,instructions, or artwork/banner
    description = DOCUMENTATION_
)


@app.get("/")
def health_read_root():
    return {"Retrieving Bibi's status report": "Activated",
            "message": "Hi hi! I'm Bibi, your cloud API key guardian! <3. Ready to protect your  API keys!"
            }

print (x)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

