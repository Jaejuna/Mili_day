import * as firebase from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyDqLsZivTrSlJZbegt57ZIpkr8p2wQCahQ",
  authDomain: "mili-day.firebaseapp.com",
  projectId: "mili-day",
  storageBucket: "mili-day.appspot.com",
  messagingSenderId: "203495632994",
  appId: "1:203495632994:web:11fbe5d72e04a0885ca13b",
  measurementId: "G-T28RD5SGEQ"
};

export default firebase.initializeApp(firebaseConfig);