import React, { useState } from 'react';
import { Client } from '@gradio/client';

const MainPage = () => {
    const [image, setImage] = useState<File | null>(null);
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    const handleImageUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0] || null;
        setImage(file);
        setResult(null);
        setError(null);

        if (file) {
            setLoading(true);
            try {
                const client = await Client.connect("BarsatK/rose-leaf-classifier");
                const result = await client.predict("/predict", { 
                    img: file, 
                });
                setResult(result.data);
                console.log(result.data);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'An error occurred');
                console.error('Error:', err);
            } finally {
                setLoading(false);
            }
        }
    };

    return (
        <>
            {image && (
                <div> 
                    <img src={URL.createObjectURL(image)} alt="Uploaded" />
                </div>
            )}
            
            <div>
                <input 
                    type="file" 
                    name="myImage" 
                    accept="image/*"
                    onChange={handleImageUpload} 
                />
            </div>

            {loading && (
                <div>
                    <p>Analyzing image...</p>
                </div>
            )}

            {error && (
                <div>
                    <p style={{ color: 'red' }}>Error: {error}</p>
                </div>
            )}

            {result && (
                <div>
                    <h3>Classification Result:</h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </>
    );
};

export default MainPage;