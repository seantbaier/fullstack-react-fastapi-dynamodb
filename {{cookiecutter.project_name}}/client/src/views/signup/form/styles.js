import { css } from '@emotion/react'

import {
  primaryColor,
  primaryColorDark,
  breakpoints,
} from '../../../styles/utils'

const signupForm = css`
  .form-container {
    display: flex;
    flex-direction: column;

    @media (min-width: ${breakpoints.md}) {
      flex-direction: row;
    }

    label {
      display: none;
    }
  }

  .error-message {
    color: red;
    display: block;
    margin-top: 10px;
    font-style: italic;
    font-size: 0.8rem;
  }
`

const button = css`
  width: 100%;
  height: 60px;
  margin-top: 25px;
  padding: 10px;
  box-shadow: 5px 5px 10px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background-color: ${primaryColor};
  border: none;
  color: white;
  font-size: 1.25rem;
  transition: 0.5s;

  :hover {
    background-color: ${primaryColorDark};
  }

  :focus {
    outline: none;
  }

  :disabled {
    background-color: black;
  }

  @media (min-width: ${breakpoints.md}) {
    width: 150px;
    margin-top: 0;
  }
`

export { signupForm, button }
