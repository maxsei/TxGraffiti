from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request


# from TxGraffiti.functions.make_inequalities import make_all_upper_linear_conjectures, make_all_lower_linear_conjectures
# from TxGraffiti.functions.make_inequalities import filter_conjectures, dalmatian, write_on_the_wall
# import pandas as pd
# from pyfiglet import figlet_format
# from halo import Halo
# import time
# from datetime import datetime, timedelta

app = FastAPI()
templates = Jinja2Templates(directory="templates")

__version__ = '0.0.1'


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    response = templates.TemplateResponse(
        "home.html",
        {"request": request},
    )
    return response




@app.post("/num_math_obj")
def echo(number: Annotated[str, Form()]):
    # df = pd.read_csv(f"math_data/data/{csv_name}.csv")
    # return df.to_dict()
    # return df
    # print(f"number: {number}")
    return {"number": number}
