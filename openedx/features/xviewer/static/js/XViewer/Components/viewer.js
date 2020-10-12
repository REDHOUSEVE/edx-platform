/* eslint-disable react/jsx-no-comment-textnodes */
import React from 'react';
import axios from 'axios';
import { Navbar, Nav, NavDropdown, Button } from 'react-bootstrap';
import Table from 'react-bootstrap/Table';
import Card from 'react-bootstrap/Card';
import CardDeck from 'react-bootstrap/CardDeck';
import Logo from '../logo.svg';

function callSketch(uid= "65ba4778de1843c4b18e69380b20dc67"){
    var iframe = document.getElementById( 'api-frame' );
    //var uid = '7w7pAfrCfjovwykkEeRFLGw5SXS'; // soldier (?)
    //var uid = 'd70c2d341f01493480080659d0594c78'; // Classroom
    // By default, the latest version of the viewer API will be used.

    var client = new window.Sketchfab( '1.7.1', iframe );


    // Alternatively, you can request a specific version.
    // var client = new Sketchfab( '1.7.1', iframe );

    client.init( uid, {
        success: function onSuccess( api ){
            api.start();
            api.addEventListener( 'viewerready', function() {

                // API is ready to use
                // Insert your code here
                console.log( 'Viewer is ready' );

            } );
        },
        error: function onError() {
            console.log( 'Viewer error' );
        }
    } );
}



class Viewer extends React.Component{

    constructor(props) {
        super(props);
        this.state = {
            searchName: "",
            next_page_url: null,
            previous_page_url: null,
            modelsReturned: [],
            model: "https://sketchfab.com/3d-models/44de9112ce564d35be97a06c302a2fe3"
        };
        this.search = this.search.bind(this);
        this.searchByURL = this.searchByURL.bind(this);
    }

    componentDidMount(){
        callSketch();
        this.search();
    }

    getPageByURL(url) {
      return new Promise((resolve, reject) => {
        axios.get(url,
          {headers: {
            'Authorization' : 'Token d1a2be40a3034b3794fe540de52f5c11'
          }})
          .then(resp => resolve(resp.data))
          .catch(resp => alert(resp));
      });
    }

    searchByURL(is_next_page){
      let page_url = null;
      console.log("state when calling the next page", this.state);
      is_next_page ? page_url = this.state.next_page_url : page_url = this.state.previous_page_url; // set to either next or previous
      if (page_url != null) {
        console.log("calling API");
        this.getPageByURL(page_url).then(
          results =>
              {
                  var temp = []
                  for(let i=0; i < results.results.length; i++){
                      temp.push([results.results[i].name, results.results[i].thumbnails.images[1].url, results.results[i].uid])
                  }
                  this.setState({ modelsReturned: temp, previous_page_url: results.previous, next_page_url: results.next});
              }
        )
      }
    }

   searchAPI(){
        return new Promise((resolve, reject) => {
            axios.get(`https://api.sketchfab.com/v3/search?type=models&q=${this.state.searchName}&count=6`,
            {headers: {'Authorization' : 'Token d1a2be40a3034b3794fe540de52f5c11'}})
                .then(resp => resolve(resp.data))
                .catch(resp => alert(resp));
        });
    }

    search(){
      console.log("searching")                             //call API fxn, then assign into temp icons and names, then save in state
        this.searchAPI().then(
            results =>
            {
                var temp = []
                for(let i=0; i < results.results.length; i++){
                    temp.push([results.results[i].name, results.results[i].thumbnails.images[1].url, results.results[i].uid])
                }
                this.setState({ modelsReturned: temp, previous_page_url: results.previous, next_page_url: results.next});
            }
        )
    }



    handleChange = event => {
        this.setState({
            searchName: event.target.value
        });
    }

    render(){
        return(
<div>
  <head>
    <title>Sketchfab Viewer API example</title>
  </head>
  <body>
    <div>
      <Navbar
        variant="light"
        sticky="top"
        style={{
          borderStyle: "solid",
          borderColor: "white white red white"
        }}
      >
        <Navbar.Brand href="#home">
          <img
            alt=""
            src="https://d32r2qmogsjfiy.cloudfront.net/2020/03/Redhouse-logo.png"
            width="250"
            className="d-inline-block align-top"
            style={{ marginLeft: "0.5em" }}
          />
        </Navbar.Brand>
        <Nav className="ml-auto">
          <Nav.Link href="/login">
            <Button variant="primary">Register</Button>
          </Nav.Link>
        </Nav>
      </Navbar>
    </div>
    <div>
      <img
        src="https://static.stambol.com/wordpress/wp-content/uploads/2018/05/ARVRHeadsetDesign_1640x894.jpg"
        style={{ width: "100%", height: "50%" }}
      />
    </div>

    <div class="container-flex p-5">
      <center>
        <h1 class="m-3">Model Viewer</h1>
      </center>
      <h4>Search for images to display in Virtual Reality:</h4>


        <div class="col-6 d-flex justify-content-end">
          <input
            type="text"
            class="form-control"
            placeholder="e.g. Car"
            style={{



            }}
            onChange={this.handleChange}
          />
        </div>
        <div class="col-8">
          <Button variant="danger" onClick={this.search}>
            Submit
          </Button>
        </div>


      <div class="row align-items-center">
          <iframe
            title="viewer1"
            src=""
            id="api-frame"
            allow="autoplay; fullscreen; vr"
            allowvr
            allowfullscreen
            mozallowfullscreen="true"
            webkitallowfullscreen="true"
            style={{ width: '1733px', height: '990px' }}
          />
          <div class="row align-items-end" id="results">
          <h2>Results:</h2>
               <Table responsive>
            <tbody>
              {this.state.modelsReturned.map(item => (
                <th key={item[0]}>
                <CardDeck>
                <Card>
                      <Card.Img
                          variant="top"
                          onClick={() => callSketch(item[2])}
                          src={item[1]}
                          alt={item[0]}
                          title={item[0]}
                          style={{height:'250px', width: '250px',  cursor: 'pointer'}}
                          />
                        <Card-Body>
                        <Card-Title>{item[0]}</Card-Title>
                        </Card-Body>
                        </Card>
                        </CardDeck>



                </th>
              ))}
            </tbody>
          </Table>
          <div class="row justify-content-between">
            <ul class="pagination ">
                <div class="col-6">
                  <li class="page-item" key="Previous">
                    { this.state.previous_page_url != null &&
                      <Button class="page-link" onClick={() => this.searchByURL(false)}>Prev.</Button>
                    }
                      <span class="sr-only">Previous</span>
                  </li>
                </div>
            </ul>
            <ul class="pagination ">
                <div class="col-6">
                  <li class="page-item" key="Next">
                    { this.state.next_page_url != null &&
                      <Button class="page-link" onClick={() => this.searchByURL(true)}>Next</Button>
                    }
                    <span class="sr-only">Next</span>
                  </li>
                </div>
            </ul>
          </div>

      </div>
        </div>
   </div>
  </body>
</div>

        );
    }

}


export default Viewer;
