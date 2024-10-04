// src/components/Auth/Profile.jsx
import { useEffect, useState } from 'react';
import { getProfile } from '../../api/auth';
import { getToken } from '../../utils/token';
import { useNavigate } from 'react-router-dom';

const Profile = () => {
    const [profile, setProfile] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            const token = getToken();
            if (!token) {
                navigate('/login');
            } else {
                const data = await getProfile(token);
                setProfile(data);
            }
        };

        fetchProfile();
    }, [navigate]);

    if (!profile) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>Profile</h2>
            <p>Username: {profile.username}</p>
            <p>Email: {profile.email}</p>
        </div>
    );
};

export default Profile;
