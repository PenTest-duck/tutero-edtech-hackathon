import React from "react";
import Header from "@/components/Header";
import Main from "@/components/Main";
import Footer from "@/components/Footer";

function Index() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <Main />
      <Footer />
    </div>
  );
}

export default Index;
