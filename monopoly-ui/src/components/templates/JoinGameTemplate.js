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
        font-size:12px;
    }
`


export const JoinGameTemplate = ({isRegisterScreenVisible,cancelBtn,loginBtn,registerBtn,userNameInputText,passwordInputText,characterSelectionDropdown,imageId,toggletoRegisterBtn,toggleToLoginBtn,registerForm,loginForm})=> {
   
   

    return (
            <React.Fragment>
                {isRegisterScreenVisible && 
    
                    <StyledMenuForm {...registerForm}>   
                        <RegisterPlayerMenu
                            cancelBtn={cancelBtn}
                            registerBtn={registerBtn}
                            userNameInputText={userNameInputText}
                            passwordInputText={passwordInputText}
                            characterSelectionDropdown={characterSelectionDropdown}
                            imageId={imageId}
                        />
                        <StyledSpan>--OR--</StyledSpan>
                        <MonopolyDealButton {...toggleToLoginBtn} />
                    </StyledMenuForm>
                      
                    
                }
                {!isRegisterScreenVisible && 
                    
                    <StyledMenuForm {...loginForm}>
                        
                        <LoginPlayerMenu 
                            cancelBtn={cancelBtn}
                            loginBtn={loginBtn}
                            userNameInputText={userNameInputText}
                            passwordInputText={passwordInputText}
                        />
                        <StyledSpan>--OR--</StyledSpan>
                        <MonopolyDealButton {...toggletoRegisterBtn} />
                    </StyledMenuForm>
                }
            </React.Fragment>

    )
}

