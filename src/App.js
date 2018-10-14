import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
//import logo from './logo.svg';
import './App.css';
import './bootstrap.css';

import HomePage from './home/HomePage.js';
import SettingsPage from './settings/SettingsPage.js';

function home_bar(path, text){
  return (
    <div className="nav-item" key={path}>
      <Link className="nav-link" to={path}>{text}</Link>
    </div>
  )
}

class App extends Component {
  constructor(props){
    super(props);

    this.state = {
      mode: "normal",
    }


  }

  toggleEdit(e){
    console.log("goteem")
    this.setState({mode: (this.state.mode == "normal")?"edit":"normal"});
  }

  render() {
    let navItems = [
      ["/",         "Home"],
      ["/settings", "Settings"],
    ].map((pair)=>home_bar.apply(null, pair));

    return (
      <div className="App">
        <header className="App-header">

        </header>
      </div>
    );
  }
}

export default App;
