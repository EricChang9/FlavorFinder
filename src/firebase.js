// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getStorage } from 'firebase/storage'
import { getDatabase } from 'firebase/database'

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDpOXyF9uflUrcZcs3FqJUpIsb-MX0GzDw",
  authDomain: "meal-planning-cc508.firebaseapp.com",
  projectId: "meal-planning-cc508",
  storageBucket: "meal-planning-cc508.appspot.com",
  messagingSenderId: "442765133676",
  appId: "1:442765133676:web:27361c67ee0291bb38d549",
  measurementId: "G-LBJPBC8B88"
};

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);
const storage = getStorage(firebase);
const database = getDatabase(firebase);

export {firebase, storage, database}