import React,{useReducer,useState,createContext,useEffect} from 'react'
import {ActionTypes} from "../common/constants";
import {getGame,createGame} from '../api/gamesApi';

export const GameContext = createContext();

const gameInitState = {
  game:null,
  errors:null
};


const gameReducer = (state,action)=>{
    switch(action.type){
        case ActionTypes.CreateResource:
          return {...state,game:action.game,errors:action.errors};
        case ActionTypes.GetResource:
          break;
    }

}

export const GameContextProvider = ({children}) => {
 
  const [gameState,gameDispatch] = useReducer(gameReducer,gameInitState)

  return (
    <GameContext.Provider
    
      value={{gameState,gameDispatch}}>
      {children}
    </GameContext.Provider>
  );
};
  