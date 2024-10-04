// src/App.jsx
import NavBar from './components/Layout/NavBar';
import AppRouter from './router'; // Ensure this imports your router setup

const App = () => {
    return (
        <div>
            <NavBar />  {/* Include the NavBar here */}
            <AppRouter /> {/* Set up your routes */}
        </div>
    );
};

export default App;
