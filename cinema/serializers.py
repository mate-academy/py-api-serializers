from rest_framework import serializers

from cinema.models import Genre, Actor, Movie, Order, Ticket, CinemaHall, MovieSession



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)
    genres = GenreSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ('id','title', 'description', 'actors', 'genres')

class MovieListSerializer(serializers.ModelSerializer):

    actors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'actors',
            'genres',
        ]



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ('id','name','rows','seats_in_row', 'capacity')


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='movie.title', read_only=True)

    cinema_hall = serializers.CharField(source='cinema_hall.name', read_only=True)
    cinema_hall_capacity = serializers.CharField(source='cinema_hall.capacity', read_only=True)

    class Meta:
        model = MovieSession
        fields = ('id','show_time', 'movie_name', 'cinema_hall', 'cinema_hall_capacity')

class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie       = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ('id', 'show_time', 'movie', 'cinema_hall')