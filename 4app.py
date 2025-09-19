import React, { useState, useRef } from 'react';
import { Transition } from '@headlessui/react';

const App = () => {
  const [showMainContent, setShowMainContent] = useState(false);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [isLoginView, setIsLoginView] = useState(true);
  const [uploadedImageUrl, setUploadedImageUrl] = useState(null);
  const fileInputRef = useRef(null);

  const handleAuthClick = () => {
    setShowAuthModal(true);
  };

  const handleShowMainContent = () => {
    setShowMainContent(true);
  };

  const handleGoHome = () => {
    setShowMainContent(false);
    // Scroll to the top of the page when going back to the hero section
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const closeModal = () => {
    setShowAuthModal(false);
  };

  const staff = {
    name: 'Cecilia Wamburu',
    title: 'Psychiatric Mental Health Nurse Practitioner (PMHNP-BC)',
    bio: 'Cecilia is a compassionate and dedicated professional with extensive experience in managing complex mental health issues. She specializes in providing personalized care through a combination of medication management and psychotherapy.',
    avatarUrl: 'https://placehold.co/400x400/10b981/ffffff?text=Upload+Photo',
  };

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const fileUrl = URL.createObjectURL(file);
      setUploadedImageUrl(fileUrl);
    }
  };

  return (
    <div className="bg-gray-50 font-sans antialiased text-gray-800">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          {/* Logo and Site Name */}
          <div className="flex items-center space-x-3">
            <svg
              className="h-10 w-10 text-emerald-600"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2Z"
                fill="#D1FAE5"
              />
              <path
                d="M16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16C14.2091 16 16 14.2091 16 12Z"
                fill="#6EE7B7"
              />
              <path
                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                stroke="#047857"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M12 16C14.2091 16 16 14.2091 16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16Z"
                fill="#6EE7B7"
              />
            </svg>
            <span className="text-2xl font-bold text-gray-900 tracking-wide">Thrive Wellness</span>
          </div>
          {/* Navigation and Buttons */}
          <nav className="hidden md:flex items-center space-x-6">
            <a href="#" onClick={handleGoHome} className="text-gray-600 hover:text-emerald-600 transition-colors font-medium">Home</a>
            <a href="#about" className="text-gray-600 hover:text-emerald-600 transition-colors font-medium">About Us</a>
            <a href="#services" className="text-gray-600 hover:text-emerald-600 transition-colors font-medium">Services</a>
            <a href="#staff" className="text-gray-600 hover:text-emerald-600 transition-colors font-medium">Our Team</a>
            <a href="#contact" className="text-gray-600 hover:text-emerald-600 transition-colors font-medium">Contact</a>
            <button onClick={handleAuthClick} className="bg-emerald-600 text-white font-semibold py-2 px-6 rounded-full shadow-lg hover:bg-emerald-700 transition-colors">Login / Register</button>
          </nav>
        </div>
      </header>

      {/* Conditional Hero Section */}
      {!showMainContent && (
        <section id="hero" className="bg-gradient-to-r from-emerald-600 to-blue-700 text-white py-48 relative overflow-hidden flex flex-col items-center justify-center text-center">
          <div className="container mx-auto px-4 max-w-4xl">
            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight tracking-tight drop-shadow-lg">
              Empowering Your Mental Well-being.
            </h1>
            <p className="mt-6 text-lg md:text-xl font-light max-w-2xl mx-auto opacity-90">
              Providing compassionate and personalized care with a team of dedicated mental health professionals.
            </p>
            <div className="mt-12 animate-bounce">
              <button onClick={handleShowMainContent} className="inline-block bg-amber-400 text-gray-900 font-bold py-3 px-8 rounded-full shadow-lg hover:bg-amber-500 transition-colors transform hover:scale-105">
                Explore Our Care
              </button>
            </div>
          </div>
        </section>
      )}

      {/* Main Content (Conditionally rendered) */}
      {showMainContent && (
        <React.Fragment>
          {/* About Us Section */}
          <section id="about" className="py-20 bg-white">
            <div className="container mx-auto px-4 max-w-6xl">
              <h2 className="text-4xl font-extrabold text-center mb-16 text-gray-900">About Thrive Wellness</h2>
              <div className="flex flex-col md:flex-row items-center md:space-x-12">
                <div className="md:w-1/2">
                  <p className="text-gray-600 text-lg leading-relaxed mb-6">
                    At Thrive Mental Wellness, our mission is to provide a safe, supportive, and compassionate environment for individuals seeking to improve their mental health. We believe in a holistic approach that combines evidence-based practices with personalized care.
                  </p>
                  <p className="text-gray-600 text-lg leading-relaxed">
                    Our team is dedicated to helping you navigate life's challenges, achieve your goals, and live a fulfilling life. We are committed to your well-being and are here to partner with you every step of the way.
                  </p>
                </div>
                <div className="md:w-1/2 mt-12 md:mt-0">
                  <h3 className="text-3xl font-bold text-gray-900 mb-6">Our Core Values</h3>
                  <ul className="text-gray-600 space-y-4">
                    <li className="flex items-start space-x-3">
                      <span className="text-emerald-500 mt-1">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                          <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 3.866-3.899 7-8.75 7s-8.75-3.134-8.75-7S4.25 3.5 9.101 3.5 19.5 6.634 19.5 10.5z" />
                        </svg>
                      </span>
                      <div>
                        <h4 className="font-semibold text-xl text-gray-900">Compassion</h4>
                        <p className="mt-1 text-base">We treat every individual with empathy, respect, and a deep understanding of their unique journey.</p>
                      </div>
                    </li>
                    <li className="flex items-start space-x-3">
                      <span className="text-blue-500 mt-1">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M12 18a9 9 0 110-18 9 9 0 010 18z" />
                        </svg>
                      </span>
                      <div>
                        <h4 className="font-semibold text-xl text-gray-900">Excellence</h4>
                        <p className="mt-1 text-base">We are committed to providing the highest quality of care through continuous learning and professional development.</p>
                      </div>
                    </li>
                    <li className="flex items-start space-x-3">
                      <span className="text-amber-500 mt-1">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M12 21a9 9 0 010-18" />
                          <path strokeLinecap="round" strokeLinejoin="round" d="M21 12a9 9 0 01-18 0" />
                          <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 15.75l-4.5-4.5L7.5 7.5M15.75 8.25l4.5 4.5L16.5 16.5" />
                        </svg>
                      </span>
                      <div>
                        <h4 className="font-semibold text-xl text-gray-900">Integrity</h4>
                        <p className="mt-1 text-base">We maintain the highest ethical standards, ensuring trust, confidentiality, and transparency in all our interactions.</p>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </section>

          {/* Services Section */}
          <section id="services" className="py-20 bg-gray-100">
            <div className="container mx-auto px-4 max-w-6xl">
              <h2 className="text-4xl font-extrabold text-center mb-16 text-gray-900">Our Professional Services</h2>
              <div className="grid md:grid-cols-3 gap-10">
                {/* Service Card 1 */}
                <div className="bg-white p-8 rounded-xl shadow-lg border-t-4 border-emerald-500 text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                  <div className="w-20 h-20 mx-auto bg-emerald-100 rounded-full flex items-center justify-center text-emerald-600">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M16.5 15.5l-4-4.5v-2" />
                    </svg>
                  </div>
                  <h3 className="mt-8 text-2xl font-semibold text-gray-900">Medication Management</h3>
                  <p className="mt-4 text-gray-600 leading-relaxed">Expert psychiatric care and medication management for a wide range of mental health conditions.</p>
                </div>

                {/* Service Card 2 */}
                <div className="bg-white p-8 rounded-xl shadow-lg border-t-4 border-blue-500 text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                  <div className="w-20 h-20 mx-auto bg-blue-100 rounded-full flex items-center justify-center text-blue-600">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M17 20h-4a2 2 0 01-2-2V7a2 2 0 012-2h4a2 2 0 012 2v11a2 2 0 01-2 2z" />
                      <path strokeLinecap="round" strokeLinejoin="round" d="M12 2v4m0 16v-4m-7-5a2 2 0 01-2-2v-2a2 2 0 012-2h4a2 2 0 012 2v2a2 2 0 01-2 2h-4z" />
                    </svg>
                  </div>
                  <h3 className="mt-8 text-2xl font-semibold text-gray-900">Psychotherapy</h3>
                  <p className="mt-4 text-gray-600 leading-relaxed">Individual, group, and family therapy to help you develop coping strategies and emotional resilience.</p>
                </div>

                {/* Service Card 3 */}
                <div className="bg-white p-8 rounded-xl shadow-lg border-t-4 border-amber-500 text-center transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                  <div className="w-20 h-20 mx-auto bg-amber-100 rounded-full flex items-center justify-center text-amber-600">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path d="M10 20.25c.08-.43 0-.84-.5-1.25L5 14.5m14.5 5.75c-.08-.43 0-.84-.5-1.25l-4-4.5m-5 0l4-4.5M12 6.5l-4 4.5M12 10.5l4-4.5M12 6.5v-4M12 10.5v-4" />
                    </svg>
                  </div>
                  <h3 className="mt-8 text-2xl font-semibold text-gray-900">Telehealth Sessions</h3>
                  <p className="mt-4 text-gray-600 leading-relaxed">Secure and convenient online sessions from the comfort of your own home, wherever you are.</p>
                </div>
              </div>
            </div>
          </section>

          {/* Staff Profiles Section */}
          <section id="staff" className="py-20 bg-white">
            <div className="container mx-auto px-4 max-w-6xl text-center">
              <h2 className="text-4xl font-extrabold text-center mb-16 text-gray-900">Meet Our Dedicated Team</h2>
              <div className="flex justify-center">
                <div className="bg-gray-100 p-8 rounded-xl shadow-lg border-t-4 border-emerald-400 text-center max-w-sm w-full transform transition-transform duration-300 hover:scale-105 hover:shadow-xl">
                  {/* Image and Upload Button */}
                  <div className="relative w-40 h-40 mx-auto rounded-full overflow-hidden shadow-lg border-4 border-emerald-200 group">
                    <img
                      src={uploadedImageUrl || staff.avatarUrl}
                      alt={staff.name}
                      className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                    />
                    <div className="absolute inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                      <button
                        onClick={handleUploadClick}
                        className="text-white font-bold py-2 px-4 rounded-full bg-emerald-600 hover:bg-emerald-700 transition-colors"
                      >
                        Upload Photo
                      </button>
                    </div>
                  </div>
                  <input
                    type="file"
                    ref={fileInputRef}
                    onChange={handleFileChange}
                    className="hidden"
                    accept="image/*"
                  />
                  
                  <h3 className="text-3xl font-bold text-emerald-700 mt-6">{staff.name}</h3>
                  <p className="text-emerald-600 font-medium text-lg mt-1">{staff.title}</p>
                  <p className="mt-4 text-base text-gray-600 leading-relaxed">
                    {staff.bio}
                  </p>
                  <a href="#contact" className="inline-block mt-6 text-sm font-semibold text-emerald-600 hover:underline">Connect with our team</a>
                </div>
              </div>
            </div>
          </section>

          {/* Patient Portal Placeholder */}
          <section className="bg-gray-800 text-white py-20">
            <div className="container mx-auto px-4 text-center max-w-2xl">
              <h2 className="text-3xl font-bold">Your Secure Patient Portal</h2>
              <p className="mt-4 text-lg opacity-90">
                Once you log in, you will have secure access to your medical records, appointments, and direct messaging with your provider.
              </p>
              <div className="mt-6">
                <button onClick={handleAuthClick} className="inline-block bg-white text-gray-800 font-bold py-3 px-8 rounded-full shadow-lg hover:bg-gray-200 transition-colors transform hover:scale-105">
                  Access Patient Portal
                </button>
              </div>
            </div>
          </section>

          {/* Contact Section */}
          <section id="contact" className="py-20 bg-gray-50">
            <div className="container mx-auto px-4 max-w-6xl text-center">
              <h2 className="text-4xl font-extrabold text-gray-900 mb-16">Contact Us</h2>
              <p className="text-lg text-gray-600 max-w-xl mx-auto">
                Ready to book an appointment or have a question? Our team is here to help you begin your journey to wellness.
              </p>
              <div className="mt-12 flex justify-center">
                <div className="w-full max-w-md">
                  <form className="space-y-6 bg-white p-8 rounded-lg shadow-md">
                    <input type="text" placeholder="Your Name" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-colors" />
                    <input type="email" placeholder="Your Email" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-colors" />
                    <textarea placeholder="Your Message" rows="4" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-colors"></textarea>
                    <button type="submit" className="w-full bg-emerald-600 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-emerald-700 transition-colors">
                      Send Message
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </section>
        </React.Fragment>
      )}

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4 text-center text-gray-400 text-sm">
          <p>&copy; 2025 Thrive Wellness. All rights reserved.</p>
        </div>
      </footer>

      {/* Auth Modal */}
      <Transition
        show={showAuthModal}
        as={React.Fragment}
        enter="transition duration-100 ease-out"
        enterFrom="transform scale-95 opacity-0"
        enterTo="transform scale-100 opacity-100"
        leave="transition duration-75 ease-out"
        leaveFrom="transform scale-100 opacity-100"
        leaveTo="transform scale-95 opacity-0"
      >
        <div className="fixed inset-0 z-50 overflow-y-auto">
          <div className="flex items-center justify-center min-h-screen">
            <div className="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity" onClick={closeModal}></div>
            <div className="bg-white rounded-lg shadow-xl transform transition-all sm:my-8 sm:w-full sm:max-w-md p-8 relative mx-4">
              <button onClick={closeModal} className="absolute top-4 right-4 text-gray-500 hover:text-gray-800">
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>

              <div className="flex justify-center mb-6">
                <button
                  onClick={() => setIsLoginView(true)}
                  className={`py-2 px-4 font-semibold text-lg rounded-full ${isLoginView ? 'bg-emerald-600 text-white' : 'text-gray-500'}`}
                >
                  Login
                </button>
                <button
                  onClick={() => setIsLoginView(false)}
                  className={`py-2 px-4 font-semibold text-lg rounded-full ${!isLoginView ? 'bg-emerald-600 text-white' : 'text-gray-500'}`}
                >
                  Register
                </button>
              </div>

              {isLoginView ? (
                <form className="space-y-4">
                  <h3 className="text-xl font-bold text-gray-800 text-center">Login to Your Account</h3>
                  <p className="text-sm text-gray-500 text-center">Access your patient portal securely.</p>
                  <input type="email" placeholder="Email" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500" />
                  <input type="password" placeholder="Password" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500" />
                  <a href="#" className="text-sm text-emerald-600 hover:underline">Forgot Password?</a>
                  <button type="submit" className="w-full bg-emerald-600 text-white font-bold py-3 rounded-full shadow-md hover:bg-emerald-700 transition-colors">
                    Login
                  </button>
                </form>
              ) : (
                <form className="space-y-4">
                  <h3 className="text-xl font-bold text-gray-800 text-center">Create a New Account</h3>
                  <p className="text-sm text-gray-500 text-center">It only takes a moment.</p>
                  <input type="text" placeholder="Full Name" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500" />
                  <input type="email" placeholder="Email" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500" />
                  <input type="password" placeholder="Password" className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500" />
                  <button type="submit" className="w-full bg-emerald-600 text-white font-bold py-3 rounded-full shadow-md hover:bg-emerald-700 transition-colors">
                    Register
                  </button>
                </form>
              )}
            </div>
          </div>
        </div>
      </Transition>
    </div>
  );
};

export default App;
