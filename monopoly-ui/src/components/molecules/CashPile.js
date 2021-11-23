import React from 'react'
import styled from 'styled-components';
import { device } from '../../common/devices';
import { MonopolyDealLabel } from '../atoms/MonopolyDealLabel';

const StyledBorder = styled.div`
    border:2px solid white;
    @media ${device.xlarge} {
        height:200px;
    }

    @media ${device.large} { 
        height:200px;
    }
    @media ${device.medium} { 
        height:200px;

    }
    @media ${device.small} { 
        height:200px;  
    }
`;


export const CashPile = () => {
    return (
        <React.Fragment>
            <MonopolyDealLabel type="h4" text="-Cash Pile-" />
            <StyledBorder>
            </StyledBorder>
        </React.Fragment>
    )
}
