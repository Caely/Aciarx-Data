import React from "react";
import gerdau from "../../img/gerdau.png";
import style from "../Logo/logo.module.css";

function Logo() {
  return <img src={gerdau} alt="Gerdau" className={style.logo} />;
}
export default Logo;
