import React, { useState } from 'react';
import axios from 'axios';

function Crwal() {
  const [url, setUrl] = useState('');
  const [content, setContent] = useState('');

  const handleCrawl = () => {
    // Django API URL
    // const apiUrl = 'http://localhost:8000/api/crawl/';
    const apiUrl = 'http://localhost:8000/api/gpt/';

    // API 요청
    axios.get(apiUrl, { params: { url } })
      .then(response => {
        setContent(response.data.content);
      })
      .catch(error => {
        console.error('API Error:', error);
      });
  };

  return (
    <div>
      <h1>Web Crawler with React</h1>
      <input type="text" value={url} onChange={e => setUrl(e.target.value)} />
      <button onClick={handleCrawl}>Crawl</button>

      {content && (
        <div>
          <h2>Content:</h2>
          <pre>{content}</pre>
        </div>
      )}
    </div>
  );
}

export default Crwal;
