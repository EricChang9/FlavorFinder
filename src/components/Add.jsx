import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faImage } from '@fortawesome/free-solid-svg-icons';
import { ref, uploadBytesResumable, getDownloadURL } from 'firebase/storage';  
import { storage } from '../firebase';
const Add = () => {
  const [image, setImage] = useState(null);

  const handleImage = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
      setImage(reader.result);
      uploadImage(file);  
      console.log('Clicker');
    };

    if (file) {
      reader.readAsDataURL(file);
      console.log('Clicked')
      extract.main()
    }
  };

  const uploadImage = (file) => {
    const storageRef = ref(storage, `images/${file.name}`);
    const uploadTask = uploadBytesResumable(storageRef, file);

    uploadTask.on(
      'state_changed',
      (snapshot) => {
        const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        console.log(`Upload is ${progress}% done`);
      },
      (error) => {
        console.error(error);
      },
      async () => {
        const downloadURL = await getDownloadURL(uploadTask.snapshot.ref);
        console.log('File available at', downloadURL);
      }
    );
  };

  return (
    <div className='a--container'>
      <h2 className='i--title'>Meal Planner</h2>
      <div className='i--container'>
        {image && <img src={image} alt="Selected" className='i--image' />}
      </div>
      <input 
        type="file"
        accept='image/'
        onChange={handleImage}
        style={{ display: 'none' }}
        id="imageInput"
      />
      <div className="b--container">
        <label htmlFor='imageInput' className='a--button'>
          <FontAwesomeIcon icon={faImage}  className='a--icon'/>
        </label>
      </div>
    </div>
  );
}

export default Add;
