from reactpy import web
mui = web.module_from_template("react", "@mui/material")
Button = web.export(mui, 'Button')
