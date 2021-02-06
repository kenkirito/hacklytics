import { Fragment } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
// Pages Import
import Header from "./Header/Header";
import Home from "./Home page/home";

const App = () => {
  return (
    <Fragment>
      <div>
        <Router>
        <Header />
          <Switch>
            <Route exact path="/" component={Home} />
          </Switch>
        </Router>
      </div>
     
    </Fragment>
  );
};

export default App;