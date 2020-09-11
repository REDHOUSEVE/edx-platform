import React from 'react';
import ReactDOM from 'react-dom';

import {
    BrowserRouter as Router,
    Switch,
    Route,
} from 'react-router-dom';

import PanelNavbar from './containers/Navbar';


export default function Dashboard({ context }) {
    return (
        <Router basename={context.base_url} >
            <PanelNavbar />
            <Switch>
                <Route exact path='/' >
                    <div>Admin Home Page</div>
                </Route>
                <Route path='/people' >
                    <div>People Page</div>
                </Route>
                <Route path='/settings' >
                    <div>Settings Page</div>
                </Route>
            </Switch>
        </Router>
    )
}

export class RedhouseAdminDashboard {
    constructor(context) {
        ReactDOM.render(
            <Dashboard context={context} />,
            document.getElementById('root'),
        );
    }
}
