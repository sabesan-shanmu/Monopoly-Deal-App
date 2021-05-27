import React,{useState} from 'react'
import PropTypes from 'prop-types';
import {StyledMenuForm} from "../atoms/StyledMenuForm";
import {LoginPlayerMenu} from "../organisms/LoginPlayerMenu"
import {RegisterPlayerMenu} from "../organisms/RegisterPlayerMenu"
import {MonopolyDealButton} from "../atoms/MonopolyDealButton"
import {device} from '../../common/devices'
import styled from 'styled-components'


const StyledSpan = styled.div`

    @media ${device.xlarge} {
        font-size:20px;
    }
    
    @media ${device.medium} { 
        font-size:15px;
    }

    @media ${device.small} { 
        font-size:8px;
    }
`


export const JoinGameTemplate = ({isRegisterScreenVisible,cancelBtn,loginBtn,registerBtn,userNameInput,passwordInput,characterSelectionDropdown,imageId,toggletoRegisterBtn,toggleToLoginBtn})=> {
   
   

    return (
            <React.Fragment>
                {isRegisterScreenVisible && 
    
                    <StyledMenuForm>   
                        <RegisterPlayerMenu
                            cancelBtn={cancelBtn}
                            registerBtn={registerBtn}
                            userNameInput={userNameInput}
                            passwordInput={passwordInput}
                            characterSelectionDropdown={characterSelectionDropdown}
                            imageId={imageId}
                        />
                        <StyledSpan>--OR--</StyledSpan>
                        <MonopolyDealButton {...toggleToLoginBtn} />
                    </StyledMenuForm>
                      
                    
                }
                {!isRegisterScreenVisible && 
                    
                    <StyledMenuForm>
                        
                        <LoginPlayerMenu 
                            cancelBtn={cancelBtn}
                            loginBtn={loginBtn}
                            userNameInput={userNameInput}
                            passwordInput={passwordInput}
                        />
                        <StyledSpan>--OR--</StyledSpan>
                        <MonopolyDealButton {...toggletoRegisterBtn} />
                    </StyledMenuForm>
                }
            </React.Fragment>

    )
}

