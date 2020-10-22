import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

export class XViewer {
    constructor(context) {
        ReactDOM.render(
            <App context={context} />,
            document.getElementById('root'),
        );
    }
}
