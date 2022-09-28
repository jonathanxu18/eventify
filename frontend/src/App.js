import './App.css';

import Home from './Home';
import Events from './Events';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/events' element={<Events/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
