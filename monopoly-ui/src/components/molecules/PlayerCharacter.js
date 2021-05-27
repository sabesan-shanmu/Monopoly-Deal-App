import React from 'react'
import PropTypes from 'prop-types';
import styled from 'styled-components'
import {device} from "../../common/devices";
import { CharacterImage } from '../atoms/CharacterImage';
import {getBackgroundColour} from '../../common/ImageHelpers'





const StyledPlayerCharacter = styled.section`
    display:grid;
    grid-template-columns: 2fr 1fr;
    background-color:${({imageId})=>getBackgroundColour(imageId)};
    background-size: cover;
    border: 2px solid black;
    border-radius: 5px;
`;

export const PlayerCharacter = ({playerName,imageId,numberOfCardsOnHand,playerGameOrder,...props}) => { 

    return (
        <StyledPlayerCharacter imageId={imageId}>
            <CharacterImage imageId={imageId}/>
            <div>
                <div>Player Name:{playerName}</div>
                <div>Game Order:{playerGameOrder}</div>
                <div>{/** add {numberOfCardsOnHand} of Cards  */}</div>
            </div>   
        </StyledPlayerCharacter>
    )
}


PlayerCharacter.propTypes = {
    playerName:PropTypes.string,
    playerGameOrder:PropTypes.oneOf(["1","2","3","4","5","6","7","8","9","10","11","12"]),
    imageId:PropTypes.oneOf(["1","2","3","4","5","6","7","8","9","10","11","12"])
};

