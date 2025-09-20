import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// --- Pages ---
const Home = () => (
  <div className="p-10 text-center">
    <h1 className="text-4xl font-bold text-emerald-700">Thrive Mental Wellness</h1>
    <p className="mt-4 text-gray-600">
      Providing compassionate psychiatric care, psychotherapy, and medication management.
    </p>
  </div>
);

const Services = () => (
  <div className="p-10">
    <h2 className="text-3xl font-bold text-emerald-600">Our Services</h2>
    <ul className="mt-4 space-y-2 text-gray-700">
      <li>✔ Medication Management</li>
      <li>✔ Psychotherapy</li>
      <li>✔ Telehealth Sessions</li>
    </ul>
  </div>
);

const Contact = () => (
  <div className="p-10">
    <h2 className="text-3xl font-bold text-emerald-600">Contact Us</h2>
    <form className="mt-6 space-y-4 max-w-md">
      <input type="text" placeholder="Your Name" className="w-full p-3 border rounded" />
      <input type="email" placeholder="Your Email" className="w-full p-3 border rounded" />
      <textarea placeholder="Message" className="w-full p-3 border rounded"></textarea>
      <button className="w-full bg-emerald-600 text-white py-2 rounded">Send</button>
    </form>
  </div>
);

const PatientDashboard = () => (
  <div className="p-10">
    <h2 className="text-3xl font-bold">Patient Portal</h2>
    <p className="text-gray-600">View your appointments, prescriptions, and chat with staff.</p>
  </div>
);

const StaffDashboard = () => (
  <div className="p-10">
    <h2 className="text-3xl font-bold">Staff Dashboard</h2>
    <p className="text-gray-600">Upload reports, manage patient records, and update your profile.</p>
  </div>
);

const AdminDashboard = () => (
  <div className="p-10">
    <h2 className="text-3xl font-bold">Admin Dashboard</h2>
    <p className="text-gray-600">Manage staff, patients, and system settings.</p>
  </div>
);

// --- Navbar ---
const Navbar = ({ isLoggedIn, setIsLoggedIn }) => (
  <nav className="flex justify-between items-center bg-white p-4 shadow">
    <Link to="/" className="text-xl font-bold text-emerald-700">Thrive Wellness</Link>
    <div className="space-x-4">
      <Link to="/services" className="text-gray-600 hover:text-emerald-600">Services</Link>
      <Link to="/contact" className="text-gray-600 hover:text-emerald-600">Contact</Link>
      {isLoggedIn ? (
        <>
          <Link to="/patient" className="text-gray-600 hover:text-emerald-600">Patient</Link>
          <Link to="/staff" className="text-gray-600 hover:text-emerald-600">Staff</Link>
          <Link to="/admin" className="text-gray-600 hover:text-emerald-600">Admin</Link>
          <button onClick={() => setIsLoggedIn(false)} className="bg-red-500 text-white px-3 py-1 rounded">Logout</button>
        </>
      ) : (
        <button onClick={() => setIsLoggedIn(true)} className="bg-emerald-600 text-white px-3 py-1 rounded">Login</button>
      )}
    </div>
  </nav>
);

// --- App ---
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <Router>
      <Navbar isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/patient" element={<PatientDashboard />} />
        <Route path="/staff" element={<StaffDashboard />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
      <footer className="bg-gray-900 text-white text-center p-4 mt-10">
        © 2025 Thrive Mental Wellness. All rights reserved.
      </footer>
    </Router>
  );
}

export default App;
