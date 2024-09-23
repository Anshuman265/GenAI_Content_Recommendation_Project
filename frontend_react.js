
import React, { useState, useEffect } from 'react';

const ContentRecommender = () => {
    const [content, setContent] = useState('');

    useEffect(() => {
        fetch('/api/recommend')
            .then(response => response.json())
            .then(data => setContent(data.content));
    }, []);

    return (
        <div>
            <h2>Personalized Recommendation</h2>
            <p>{content}</p>
        </div>
    );
};

export default ContentRecommender;
