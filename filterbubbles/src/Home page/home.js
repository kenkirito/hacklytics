import React from "react";
import "./home.css";
import { createMuiTheme, withStyles, makeStyles, ThemeProvider } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import { green, pink, purple } from '@material-ui/core/colors';


  
  const ColorButton = withStyles((theme) => ({
    root: {
      color: theme.palette.getContrastText(pink[500]),
      backgroundColor: pink[500],
      '&:hover': {
        backgroundColor: pink[700],
      },
    },
  }))(Button);
  
  const useStyles = makeStyles((theme) => ({
    margin: {
      margin: theme.spacing(1),
      marginTop: '1%',
      borderRadius: '30px',
    },

  }));
  
 

export default function CustomizedButtons() {
    const classes = useStyles();
  return (
<>
<div>
<h1 className="text"> Input Text </h1>
<form>
  <textarea className="textarea" >Some text...</textarea>
</form>
<ColorButton variant="contained" color="primary" className={classes.margin}>
          Submit
      </ColorButton>
      </div>
      <div>
<h1 className="text_two"> Output Text </h1>
<form>
  <textarea className="textarea_two" >Some text...</textarea>
</form>
</div>
</>
  );
}



