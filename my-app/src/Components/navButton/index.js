import React from "react";

import style from "./navButton.module.css";

function NavButton({ text, iconUrl, url }) {
  return (
    <a href={url} className={style.button}>
      <img src={iconUrl} alt="Icon" className={style.margin} /> {text}
    </a>
  );
}

export default NavButton;
