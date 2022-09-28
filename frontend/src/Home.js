import {React, useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import axios from 'axios';

import './Home.css';
import { API_URL } from './constants/index';

function Home() {
    const [authUrl, setAuthUrl] = useState();

    useEffect(() => {
        axios.get('api/login')
        .then(response => {
            console.log(response);
            setAuthUrl(response.data.auth_url);
        })
        .catch(() => {
            console.log('There was an error during the API request.');
        });
    }, []);

    return (
        <Button href={authUrl}> 
            Test 
        </Button>
    );
}

export default Home;