// src/components/Layout/NavBar.jsx
import { Link } from 'react-router-dom';
import { getToken, removeToken } from '../../utils/token';
import { useNavigate } from 'react-router-dom';

const NavBar = () => {
    const token = getToken();
    const navigate = useNavigate();

    const handleLogout = () => {
        removeToken();
        navigate('/login');
    };

    return (
        <nav>
            <Link to="/signup">Signup</Link>
            <Link to="/login">Login</Link>
            {token && (
                <>
                    <Link to="/profile">Profile</Link>
                    <button onClick={handleLogout}>Logout</button>
                </>
            )}
        </nav>
    );
};

export default NavBar;
