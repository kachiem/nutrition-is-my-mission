import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import $ from 'jquery';
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
        <header className="home_bar">
        </header>
      </div>
    );
  }
} 

class Square extends React.Component {
  render() {
    return (
      <div>
      <div>
        <button className="square">
          {this.props.value}
        </button>
      </div>
      <input type="file" id="pic" accept="image/*" onclick="uploadOnChange()"/>
      <div id="filename"></div>
      <div>
        //this.button = this.button.bind
        <button className="btn btn-success" onClick="sendMessage()">Nut</button> 
      </div>
      </div>
    );
  }
}

export default App;
