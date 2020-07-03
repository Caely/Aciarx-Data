import React from "react";
import Search from "./Components/Search";
import User from "./Components/User";

import SideBar from "../src/Components/sideBar";
import Main from "./Components/Main";

function Gerdau() {
  return (
    <div>
      <SideBar></SideBar>
      <Main>
        <Search></Search>
      </Main>
    </div>
  );
}

export default Gerdau;
