"""Main FPLstat client for easy access to FPL data."""

from typing import Optional
import pandas as pd
import requests

from .api.client import DataClient


class FPLstat:
    """Main interface for accessing Fantasy Premier League data.
    
    Provides a simple interface to load, transform, and access FPL data
    as ready-to-use pandas DataFrames.
    
    Example:
        >>> from fplstat import FPLstat
        >>> fpl = FPLstat()
        >>> players_df = fpl.get_players()
        >>> teams_df = fpl.get_teams()
    """
    
    def __init__(self):
        """Initialize the FPLstat client."""
        self._data_client = DataClient()
    
    def get_players(self) -> pd.DataFrame:
        """Get DataFrame of all players with their stats.
        
        Returns:
            DataFrame with player information including stats, team, position, etc.
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.elements)
    
    def get_teams(self) -> pd.DataFrame:
        """Get DataFrame of all Premier League teams.
        
        Returns:
            DataFrame with team information including form, strength, etc.
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.teams)
    
    def get_fixtures(self) -> pd.DataFrame:
        """Get DataFrame of all fixtures for the season.
        
        Returns:
            DataFrame with fixture information including dates, scores, etc.
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.fixtures)
    
    def get_gameweeks(self) -> pd.DataFrame:
        """Get DataFrame of all gameweeks/events.
        
        Returns:
            DataFrame with gameweek information including dates, deadlines, etc.
        """
        # TODO: Transform raw data using transformers
        return pd.DataFrame(self._data_client.events)
    
    def get_player_history(self, player_id: int) -> pd.DataFrame:
        """Get detailed history for a specific player.
        
        Args:
            player_id: The FPL player ID
            
        Returns:
            DataFrame with per-gameweek stats for the player
        """
        player_data = self._data_client.get_element_summary(player_id)
        # TODO: Transform raw data using transformers
        history_data = player_data['history']
        return pd.DataFrame(history_data)
    
    def get_gameweek_live(self, gameweek: int) -> pd.DataFrame:
        """Get live stats for all players in a specific gameweek.
        
        Args:
            gameweek: The gameweek number
            
        Returns:
            DataFrame with live player stats for the gameweek
        """
        live_data = self._data_client.get_event_live(gameweek)
        # TODO: Transform raw data using transformers
        elements_data = live_data.get('elements', [])
        return pd.DataFrame(elements_data)
    
    def get_manager_team(self, manager_id: int) -> pd.DataFrame:
        """Get information about a manager's team.
        
        Args:
            manager_id: The FPL manager/entry ID
            
        Returns:
            DataFrame with manager team information
        """
        team_data = self._data_client.get_entry(manager_id)
        # TODO: Transform and structure the data appropriately
        return pd.DataFrame([team_data])
    
    def get_manager_picks(self, manager_id: int, gameweek: int) -> pd.DataFrame:
        """Get a manager's team picks for a specific gameweek.
        
        Args:
            manager_id: The FPL manager/entry ID  
            gameweek: The gameweek number
            
        Returns:
            DataFrame with the manager's picks for that gameweek
        """
        picks_data = self._data_client.get_entry_picks(manager_id, gameweek)
        # TODO: Transform raw data using transformers
        picks = picks_data.get('picks', [])
        return pd.DataFrame(picks)